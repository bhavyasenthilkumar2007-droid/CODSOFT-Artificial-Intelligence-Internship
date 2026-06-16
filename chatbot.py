print("=== Campus Assistant Bot ===")
print("Ask me about department, python, internship or exit.")

while True:
    user = input("You: ").lower()

    if user == "department":
        print("Bot: I am designed for CSE students.")
    elif user == "python":
        print("Bot: Python is beginner-friendly and widely used in AI.")
    elif user == "internship":
        print("Bot: Internships help bridge academic learning and industry practice.")
    elif user == "codsoft":
        print("Bot: CodSoft provides internship tasks to build practical skills.")
    elif user == "exit":
        print("Bot: Thank you for chatting. Goodbye!")
        break
    else:
        print("Bot: Please ask a question related to my topics.")