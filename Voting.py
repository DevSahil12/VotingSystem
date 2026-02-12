import re
class User:
    def __init__(self,voter_id,username,password,role="user",is_voted=False):
        self.voter_id=voter_id
        self.username=username
        self.password=password
        self.role=role
        self.is_voted=is_voted
    def show_details(self):
        print("\n--- USER DETAILS ---")
        print("Voter ID:", self.voter_id)
        print("Username:", self.username)
        print("Role:", self.role)
        print("Has Voted:", self.is_voted)
class VotingSystem:
    def passwordStrength(self,password):
        if len(password)<8:
            return False
        if not re.search(r"[A-Z]",password):
            return False
        if not re.search(r"[a-z]",password):
             return False
        if not re.search(r"\d",password):
            return False
        if not re.search(r"[!@#$%^&*()]",password):
            return False
        else:
            print("Password is Strong")
            return True
    def register(self):
        voter_id=input("Enter Voter ID first letter of your name + DOB")
        username=input("Enter your name")
        role = input("Enter role (user/admin): ").lower()
        if role not in ["user", "admin"]:
            print("Invalid role. Defaulting to user.")
            role = "user"
        while True:
            password=input("Create your password")
            if self.passwordStrength(password):
                break
            else:
                print("X Weak Password!")
                print("Password must contains")
                print("Enter atleast one upper letter")
                print("Enter atleast one lower letter")
                print("Enter atleast one digit")
                print("Enter atleast one special character")
                print("Please Try Again")
        with open("users.txt","a") as f:
            f.write(f"{voter_id},{username},{password},{role},False \n")
        print("Registration Successful")
    def login(self):
        username = input("Enter your name: ")
        password = input("Enter your password: ")

        with open("users.txt", "r") as f:
            for line in f:
                vid, user, pwd, role, voted = line.strip().split(",")

                if user == username and pwd == password:
                    print("Login successful")
                    return User(vid, user, pwd, role, voted == "True")

        print("Invalid credentials")
        return None
    def add_candidate(self):
        name = input("Enter candidate name: ").strip().lower()
        with open("candidates.txt", "a") as f:
             f.write(name + "\n")
        print("Candidate added successfully")
    def remove_candidate(self):
        with open("candidates.txt","r") as f:
            candidates=[line.strip() for line in f if  line.strip()]
        if not candidates:
            print("No candidates available.")
        print("\nCandidates List:")
        for i, name in enumerate(candidates,1):
            print(f"{i}.{name}")
        try:
            choice= int(input("Enter number of candidate to remove"))
            if choice < 1 or choice > len(candidates):
                print("Invalid choice")
                return
            removed=candidates.pop(choice-1)
            with open("candidates.txt","w") as f:
                for c in candidates:
                    f.write(c+"\n")
            print(f"Candidate'{removed}' removed successfully.")
        except ValueError:
            print("Please enter a valid choice")
    def cast_vote(self,user):
        if user.is_voted:
            print("You have already voted.")
            return
        print("\nAvailable Candidates:")
        with open("candidates.txt", "r") as f:
            candidates = [line.strip() for line in f]
        for c in candidates:
            print("-", c)
        choice = input("Enter candidate name: ").strip().lower()
        if choice not in candidates:
            print(" Invalid candidate.")
            return
        with open("votes.txt", "a") as f:
            f.write(f"{user.voter_id},{choice}\n")
            
        self.update_vote_status(user.voter_id, "True")
        user.is_voted = True
        print("Vote Cast Successfully")
        
    def update_vote_status(self, voter_id, new_status):
        lines = []
        with open("users.txt", "r") as f:
            lines = f.readlines()
        with open("users.txt", "w") as f:
            for line in lines:
                vid, user, pwd, role, voted = line.strip().split(",")
                if vid == voter_id:
                    f.write(f"{vid},{user},{pwd},{role},{new_status}\n")
                else:
                    f.write(line)

    def show_results(self):
        result = {}
        with open("votes.txt", "r") as f:
            for line in f:
                if line.strip() == "":
                    continue
                _, candidate = line.strip().split(",")
                result[candidate] = result.get(candidate, 0) + 1
        print("\nElection Results")
        for candidate, votes in result.items():
            print(f"{candidate} : {votes} votes")
def main():
    system = VotingSystem()
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            system.register()
        elif choice == "2":
            user = system.login()
            if user:
                user.show_details()
                if user.role == "admin":
                    while True:
                        print("\n1. Add Candidate")
                        print("2. Show Results")
                        print("3. Remove Candidate")
                        print("4. Logout")
                        admin_choice = input("Choose option: ")
                        if admin_choice == "1":
                            system.add_candidate()
                        elif admin_choice == "2":
                            system.show_results()
                        elif admin_choice == "3":
                            system.remove_candidate()
                        elif admin_choice=="4":
                            break
                        else:
                            print("Invalid option")
                else:
                    while True:
                        print("\n1. Cast Vote")
                        print("2. Logout")
                        opt = input("Choose option: ")
                        if opt == "1":
                            system.cast_vote(user)
                        elif opt == "2":
                            break
                        else:
                            print("Invalid option")
        elif choice == "3":
            break
        else:
            print("Invalid choice")
main()