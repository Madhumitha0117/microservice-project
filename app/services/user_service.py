class UserService:
    def get_user(self, user_id):
        return {
            "user_id": user_id,
            "name": "Munchkin",
            "status": "active"
        }

# Sample run
if __name__ == "__main__":
    service = UserService()
    print(service.get_user(101))