from database.actions.user_actions import UserActions


def check_if_have_rights(user) -> bool:
    user_action = UserActions()
    role = user_action.check_user_role(id_of_user=user)
    if role == 'User' or role == "Admin" or role == "Moderator":
        return True
    return False
