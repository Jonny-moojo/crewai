from edu.crew import MoojoLeadGen
import os
from mem0 import MemoryClient
import uuid

def run():
    """Run the Moojo Lead Generation crew"""
    print("Starting Moojo Lead Generation...")
    
    # Check for Mem0 API key
    if "MEM0_API_KEY" not in os.environ:
        print("Warning: MEM0_API_KEY not found in environment variables")
        return
    
    # Create identifiers
    user_id = "test_user"
    agent_id = str(uuid.uuid4())
    app_id = "moojo_lead_gen"
    run_id = str(uuid.uuid4())
    
    # Initialize memory with consumer preferences
    client = MemoryClient()
    
    # Example consumer identity conversation
    messages = [
        {"role": "user", "content": "I'm looking to do some online shopping."},
        {"role": "assistant", "content": "How comfortable are you with AI-powered shopping assistants?"},
        {"role": "user", "content": "I'm very comfortable with AI technology."},
        {"role": "assistant", "content": "Do you prefer chatting with shopping assistants or traditional browsing?"},
        {"role": "user", "content": "I enjoy chatting with AI assistants while shopping."},
        {"role": "assistant", "content": "How important is privacy when you're shopping online?"},
        {"role": "user", "content": "Privacy is very important to me, especially with payments."},
    ]
    
    # Add messages to memory with all required parameters
    print("Adding consumer preferences to memory...")
    try:
        client.add(
            messages=messages,
            user_id=user_id,
            agent_id=agent_id,
            app_id=app_id,
            run_id=run_id
        )
        print("Successfully added preferences to memory")
    except Exception as e:
        print(f"Error adding to memory: {str(e)}")
    
    # Create crew with memory configuration
    crew_instance = MoojoLeadGen(
        user_id=user_id,
    ).crew()
    
    # Run the crew
    print("\nRunning crew with memory access...")
    result = crew_instance.kickoff()
    return result

if __name__ == "__main__":
    result = run()
    print("\nResults:")
    print(result)
