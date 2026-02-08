class classandfunctions():
    def subFields():
        subjects = ('Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','NLP')
        print("Sub-fields in AI are as below:")
        for sub in subjects:
            print(sub)

    def oddEven():
        num=int(input("Enter the number: "))
        if(num % 2 != 0):
            print(num,"-The given number is ODD Number")
        else:
            print(num,"-The given number is EVEN Number")

    def Elegible():
        gender = input("Please enter your gender (M/F): ")
        age=int(input("Enter your Age: "))
        if gender == "M":
            if age>=21:
                print("Congratualtions, you're ELIGIBLE for Marriage")
            else:
                print("Not Eligible")
        elif gender == "F":
            if age>=18:
                print("Congratualtions, you're ELIGIBLE for Marriage")
            else:
                print("Not Eligible")
                
    def percentage():
        Math = int(input("Enter your marks in Math: "))
        Sci = int(input("Enter your marks in Science: "))
        Soc = int(input("Enter your marks in Social Studies: "))
        Eng = int(input("Enter your marks in English: "))
        Tam = int(input("Enter your marks in Tamil: "))
        total = (Math+Sci+Soc+Eng+Tam)
        percentage = (total/500)*100
        print("You're total marks in 10th board exam is", total)
        print("You're percentage in 10th board exam is:", float(percentage))

    def area():
        height = int(input("Enter the height of the triangle: "))
        breadth = int(input("Enter the breadth of the triangle: "))
        area = (height*breadth)/2
        print ("The area of triangle is:", area)
    def perimeter():
        l= int(input("Enter the length of the triangle: "))
        b= int(input("Enter the breadth of the triangle: "))
        h= int(input("Enter the height of the triangle: "))
        peri=l+b+h
        print ("The perimeter of triangle is:", peri)