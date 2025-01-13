from edu.crew import crew

def run():
    """Run the Moojo Lead Generation crew"""
    print("Starting Moojo Lead Generation...")
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    result = run()
    print("\nResults:")
    print(result)
