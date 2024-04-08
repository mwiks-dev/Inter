def mask(first_name, last_name, date_of_birth, email):
    def mask_string(string, is_date= False):
        if not is_date:
            return string[:2] + '*' * (len(string) - 2)
        else:
            year, month, day = string.split('-')
            masked_year = year[:2] + '**'
            masked_month = month[0] + '*'
            masked_day = day[0] + '*'
            return '-'.join([masked_year, masked_month, masked_day])  
    masked_first_name = mask_string(first_name)
    masked_last_name = mask_string(last_name)
    masked_dob = mask_string(date_of_birth, is_date=True)
    masked_email = mask_string(email)

    return {"first_name": masked_first_name,
            "second_name": masked_last_name,
            "date_of_birth": masked_dob,
            "email": masked_email}
    
    

print(mask('Maryann','Mwikali',"1997-02-21",'mwikali119@gmail.com'))
