from utils import get_openai_api_key
import autogen

OPENAI_API_KEY = get_openai_api_key()

llm_config = {"model": "gpt-4o-mini"}

# Define Task
task = "Summarize the legal text, analyze the case under Indian law, and suggest legal solutions."

# Define Agents
victim = autogen.ConversableAgent(
    name="victim",
    system_message='''
        You are the victim of a legal case. Your role is to provide all necessary details of the case 
        to the junior lawyer. If clarification is needed, respond with precise answers. Once the case analysis is complete, 
        review the final advice from the senior lawyer."
         Victim Information:
Full Name: Jane Doe
Contact Information: janedoe@email.com, (555) 123-4567
Age: 34
Relevant Background: Graphic designer, lives alone, no prior legal issues
2. Incident Description:
Date and Time of Incident: March 15, 2023, at approximately 8:30 PM
Location of Incident: Central Park, New York, NY
Detailed Account of the Incident: The victim was walking alone when an unknown individual approached her, demanded her belongings, and assaulted her when she refused. The attacker fled, and bystanders called 911.
Injuries Sustained: Bruises on arms and legs, emotional distress, mild concussion
3. Legal Aspects:
Type of Case: Assault and robbery
Charges Filed: No charges yet; police report filed
Current Legal Status: NYPD is investigating, but no suspect has been identified yet
4. Witness Information:
Witness Names and Contact Info:
John Smith – (555) 987-6543
Sarah Brown – (555) 234-5678
Statements from Witnesses: Both saw the incident and confirmed that the attacker was a male wearing a black hoodie and jeans. They are willing to provide police statements.
5. Evidence:
Photos, Reports, Medical Records:
Photos of injuries from the victim’s phone
Medical report from emergency room visit
Police report number: NYPD-2023-04567
Other Supporting Documentation: Surveillance footage from a nearby store showing the attacker running away
6. Victim’s Needs:
What the Victim Seeks:
Legal representation to ensure the attacker is charged
Assistance with obtaining a restraining order (if suspect is found)
Immediate Concerns: Victim is afraid of retaliation and needs advice on self-defense and security measures''',
    llm_config=llm_config,
    human_input_mode='NEVER'
    )

junior_lawyer = autogen.ConversableAgent(
    name="junior_lawyer",
    system_message=(
        "You are a junior lawyer. Your job is to: "
        "1. Analyze the case details shared by the victim."
        "2. Propose a legal solution under Indian law."
        "3. Send your analysis to the senior lawyer for review."
        "4. Incorporate feedback from the senior lawyer and finalize the solution."
    ),
    llm_config=llm_config,
    human_input_mode='NEVER'
)

senior_lawyer = autogen.ConversableAgent(
    name="senior_lawyer",
    system_message=(
        "You are a senior lawyer with expertise in Indian law. Your role is to: "
        "1. Review the junior lawyer’s case analysis."
        "2. Identify any weaknesses, loopholes, or missing points."
        "3. Provide constructive feedback to the junior lawyer for improvement."
        "4. Approve the final solution and send it back to the victim."
    ),
    llm_config=llm_config,
    human_input_mode='NEVER'
)

# Define Group Chat Workflow
groupchat = autogen.GroupChat(
    agents=[victim, junior_lawyer, senior_lawyer],
    messages=[],
    max_round=10  # Prevent endless loops
)

manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Initiate the Chat
groupchat_result = victim.initiate_chat(
    manager,
    message=task  # Corrected the argument (was incorrectly written as "manager=task")
)
