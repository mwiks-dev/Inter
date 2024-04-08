first_name = input('Enter your first name:' )
last_name = input('Enter your last name:' )
date_of_birth = input('Enter your date of birth in the format yyyy-mm-dd:' )
mobile_number = input('Enter your mobile number:' )

def mask(first_name, last_name, date_of_birth, email):
    def mask_string(string):
        masked = string[:2]
        for char in string[2:]:
            if char == '-':
                masked += '-'
            else:
                masked += '*'

        return masked
    masked_first_name = mask_string(first_name)
    masked_last_name = mask_string(last_name)
    masked_dob = mask_string(date_of_birth)
    masked_email = mask_string(email)

    return {"first_name": masked_first_name,
            "second_name": masked_last_name,
            "date_of_birth": masked_dob,
            "email": masked_email}
    
    

mask()
