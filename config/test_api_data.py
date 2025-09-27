class RESPONSE_TEXT():
    LOGIN_USED = "User already exists"
    MISSING_REQUIRED_FIELD = "Email, password and name are required fields"
    FAILED_LOGIN = "email or password are incorrect"
    NON_AUTHORIZED = 'You should be authorised'
    EMPTY_LIST_INGREDIENTS = 'Ingredient ids must be provided'

class TEST_DATA():
    INVALID_LOGIN_DATA =  {
            "email": " ",
            "password": " "
        }
    VALID_INGREDIENTS = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
    INVALID_INGREDIENTS = {
        "ingredients": ["invalidIng123", "invalidIng321"]}
    EMPTY_LIST_INGREDIENTS = {
        "ingredients": []}
