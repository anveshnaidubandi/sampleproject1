print("""Hello,
 Welcome to State Bank of India
 Please insert your card""")

print("""Hi,Please do not Remove your Chip Card.
 Leave your card inserted during
 the Entire Transaction""")

print("""Please Select your language""")
dic={1:'English',
     2:'Hindi'}
print(dic)
d=dic[int(input('Choose Above:'))]
if d=='English':
  print('Enter Any Number Between 10 and 99 for eg:"25"')
  e=int(input())
  if (e>=10 and e<=99):
    dic1={1:'Yes',2:'No'}
    print(dic1)
    d1=dic1[int(input())]
    if d1==dic1[1]:
      dic2={1:'Please Enter Your Pin',
            2:'Pin Generation'}
      print(dic2)
      d2=dic2[int(input('Choose Above:'))]
      if d2==dic2[1]:
        e1=int(input('Enter Your Pin:'))
        if e1==1352:
          print("Please Choose 'Banking' for Cash Withdrawal.")
          dic3={1:'REGISTERATION',
                2:'BANKING',
                3:'MINI STATEMENT',
                4:'BALANCE INQUIRY',
                5:'SERVICE',
                6:'TRANSFER',
                7:'QUICK CASH'}
          print(dic3)
          d3=dic3[int(input('Choose Above:'))]
          if d3==dic3[1]:
            print('ab1')
          if d3==dic3[2]:
            dic4={1:'DEPOSITE',
                  2:'FAST CASH',
                  3:'WITHDRAWAL',
                  4:'PIN CHANGE',
                  5:'BALANCE INQUIRY',
                  6:'OTHERS',
                  7:'MINI STATEMENT'}
            print(dic4)
            d4=dic4[int(input('Choose Above:'))]
            if d4==dic4[1]:
              pass
            if d4==dic4[2]:
              print('Please Enter Your New Pin')
              e4=int(input())
              if e4==1234:
                print('Please Re-Enter Your Pin')
                e5=int(input())
                if e5==1234:
                  print('Your Transaction is being Processed Please Wait..')
                  print('Transaction Complete')
                  print('Please Take Card')
            if d4==dic4[3]:
              print('Please Select Account Type')
              dic5={1:'KCC',
                    2:'CURRENT',
                    3:'SAVINGS'}
              print(dic5)
              d5=dic5[int(input('Choose Above:'))]
              if d5==dic5[1]:
                pass
              if d5==dic5[2]:
                pass
              if d5==dic5[3]:
                print('''Please Enter Amount.(Cash Available:Rs.100,Rs.200,Rs.500,Rs.2000)''')
                e2=int(input('Rs.'))
                dic6={1:'Yes',
                      2:'No'}
                print(dic6)
                d6=dic6[int(input('Choose Above:'))]
                if d6==dic6[1]:
                  print('''Your Transaction is being Processed.Please Wait..''')
                  print('Please Collect Cash')
                  print('Transaction complete:')
                  print('AVAILABLE BALANCE:')
                if d6==dic6[2]:
                  pass
            else:
              pass
          if d3==dic3[3]:
            print('Please Select Account Type')
            dic10={1:'KCC',
                   2:'CURRENT',
                   3:'SAVINGS'}
            print(dic10)
            d10=dic10[int(input('Choose Above:'))]
            if d10==dic10[1]:
              pass
            if d10==dic10[2]:
              pass
            if d10==dic10[3]:
              print('Your Transaction is being Processed Please Wait..')
              print('Please Take Your Card')
          elif d3==dic3[4]:
            print('AB4')
          elif d3==dic3[5]:
            print('ab5')
          elif d3==dic3[6]:
            print('ab6')
          elif d3==dic3[7]:
            print('ab7')
        else:
          print('You Entered Wrong Pin')
    elif d2==dic2[2]:
      print('Please Enter Your Account Number')
      e2=int(input())
      if e2==12345678912:
        dic7={1:'Press if Correct',
            2:'Press if Not Correct'}
        print(dic7)
        d7=dic7[int(input())]
        if d7==dic7[1]:
          print('Please Enter Your 10 digit Mobile Number')
          e3=int(input())
          if e3==9553495917:
            dic8={1:'Press if Correct',
                  2:'Press if Not Correct'}
            print(dic8)
            d8=dic8[int(input())]
            if d8==dic8[1]:
              print('Dear Customer,State Bank appreciates you for the green initiative.Pin shall be shortly delivered to your registered  number on success of your transaction')
              dic9={1:'Confirm',
                    2:'Cancel'}
              print(dic9)
              d9=dic9[int(input())]
              if d9==dic9[1]:
                print('Your Transaction is being Processed Please Wait..')
                print('Transaction Complete.')
                print('Please Take Your Card')
            else:
              print('Transaction Cancel1')
        else:
          print('Transaction Cancel2')
      else:
        print('Transaction Cancel3')
    else:
      print('Transaction Cancel4')
  else:
      print('Transaction Cancel5')
else:
  print('hindi')

