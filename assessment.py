print("\033[3mBy Oyebamire Oluwaseun\033[0m")
name = input("Please enter your full name: ")
print(f"Good day Mr. or Mrs.{name}, please follow the set guidelines.")
print("Please input: \n \"0\" for Single Filing\n \"1\" for Married Filing Jointly or Qualifying Widow(er)\n \"2\" for Married Filing Separately and\n \"3\" for Head of Household")


def get_tax():

    filing_status = int(input("Filing status: "))
    taxable_income = float(input("Taxable income: "))
    if taxable_income < 0:
        return "Taxable Income must be a value greater than 0"

    if filing_status == 0:
        if taxable_income <= 8350:
            tax_0 = 0.1 * taxable_income                #"tax_0" here is used to indicate what filing case it applies yo
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_0:.2f} dollars."
        elif taxable_income <= 33950:
            assist_0 = taxable_income - 8350  #named assist here for readability in future code writing
            tax_0_1 = (0.1 * 8350) + (0.15 * assist_0)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_0_1:.2f} dollars."
        elif taxable_income <= 82250:
            assist_0_1 = taxable_income - 33950
            tax_0_2 = (0.15 * 33950) + (0.25 * assist_0_1)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_0_2:.2f} dollars."
        elif taxable_income <= 171550:
            assist_0_2 = taxable_income - 82250
            tax_0_3 = (0.25 * 82250) + (0.28 * assist_0_2)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_0_3:.2f} dollars."
        elif taxable_income <= 372950:
            assist_0_3 = taxable_income - 171550
            tax_0_4 = (0.28 * 171550) + (0.33 * assist_0_3)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_0_4:.2f} dollars."
        elif taxable_income > 372950:
            assist_0_4 = taxable_income - 372950
            tax_0_5 = (0.33 * 372950) + (0.35 * assist_0_4)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_0_5:.2f} dollars."
        else:
            return f"Oops, there seems to be an error, please re-input your taxable income."

    elif filing_status == 1:
        if taxable_income <= 16700:
            tax_1 = 0.1 * taxable_income                #"tax_1" here is used to indicate what filing case it applies to
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_1:.2f} dollars."
        elif taxable_income <= 67900:
            assist_1 = taxable_income - 16700  #named assist here for readability in future code writing
            tax_1_1 = (0.1 * 16700) + (0.15 * assist_1)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_1_1:.2f} dollars."
        elif taxable_income <= 137050:
            assist_1_1 = taxable_income - 67900
            tax_1_2 = (0.15 * 67900) + (0.25 * assist_1_1)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_1_2:.2f} dollars."
        elif taxable_income <= 208850:
            assist_1_2 = taxable_income - 137050
            tax_1_3 = (0.25 * 137050) + (0.28 * assist_1_2)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_1_3:.2f} dollars."
        elif taxable_income <= 372950:
            assist_1_3 = taxable_income - 208850
            tax_1_4 = (0.28 * 208850) + (0.33 * assist_1_3)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_1_4:.2f} dollars."
        elif taxable_income > 372950:
            assist_1_4 = taxable_income - 372950
            tax_1_5 = (0.33 * 372950) + (0.35 * assist_1_4)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_1_5:.2f} dollars."
        else:
            return f"Oops, there seems to be an error, please re-input your taxable income."

    elif filing_status == 2:
        if taxable_income <= 8350:
            tax_2 = 0.1 * taxable_income                #"tax_2" here is used to indicate what filing case it applies to
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_2:.2f} dollars."
        elif taxable_income <= 33950:
            assist_2 = taxable_income - 8350  #named assist here for readability in future code writing
            tax_2_1 = (0.1 * 8350) + (0.15 * assist_2)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_2_1:.2f} dollars."
        elif taxable_income <= 68525:
            assist_2_1 = taxable_income - 33950
            tax_2_2 = (0.15 * 33950) + (0.25 * assist_2_1)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_2_2:.2f} dollars."
        elif taxable_income <= 104425:
            assist_2_2 = taxable_income - 68525
            tax_2_3 = (0.25 * 68525) + (0.28 * assist_2_2)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_2_3:.2f} dollars."
        elif taxable_income <= 186475:
            assist_2_3 = taxable_income - 104425
            tax_2_4 = (0.28 * 104425) + (0.33 * assist_2_3)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_2_4:.2f} dollars."
        elif taxable_income > 186475:
            assist_2_4 = taxable_income - 186475
            tax_2_5 = (0.33 * 186475) + (0.35 * assist_2_4)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_2_5:.2f} dollars."
        else:
            return f"Oops, there seems to be an error, please re-input your taxable income."

    elif filing_status == 3:
        if taxable_income <= 11950:
            tax_3 = 0.1 * taxable_income                #"tax_3" here is used to indicate what filing case it applies to
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_3:.2f} dollars."
        elif taxable_income <= 45500:
            assist_3 = taxable_income - 11950  #named assist here for readability in future code writing
            tax_3_1 = (0.1 * 11950) + (0.15 * assist_3)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_3_1:.2f} dollars."
        elif taxable_income <= 117450:
            assist_3_1 = taxable_income - 45500
            tax_3_2 = (0.15 * 45500) + (0.25 * assist_3_1)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_3_2:.2f} dollars."
        elif taxable_income <= 190200:
            assist_3_2 = taxable_income - 117450
            tax_3_3 = (0.25 * 117450) + (0.28 * assist_3_2)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_3_3:.2f} dollars."
        elif taxable_income <= 372950:
            assist_3_3 = taxable_income - 190200
            tax_3_4 = (0.28 * 190200) + (0.33 * assist_3_3)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_3_4:.2f} dollars."
        elif taxable_income > 372950:
            assist_3_4 = taxable_income - 372950
            tax_3_5 = (0.33 * 372950) + (0.35 * assist_3_4)
            return f"Good day Mr. or Mrs.{name}, you will be taxed {tax_3_5:.2f} dollars."
        else:
            return f"Oops, there seems to be an error, please re-input your taxable income."
    else:
        return f"Hmm... There seems to be an error, please re-input your filing status and follow the set guidelines"

print(get_tax())
#Thank you for your time ;>