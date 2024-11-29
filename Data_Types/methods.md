## String methods

![str_11](images/str_11.png)    

***Index() Method***   
Gets the index of the given character or substring. 

![str_12](images/str_12.png)  


*!Index Method just retiúns he first occurance of the given parameter*

![str_13](images/str_13.png) 

***Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious".***
````
word = "supercalifragilisticexpialidocious"
print(word.index('x'))

````
*If the substring is not there, method returns a value error.*
![str_14](images/str_14.png)

***Use "in" keyword to avoid getting error ba trying to get index of a substring.***

![str_15](images/str_15.png)

Lets replace the old domain with newones of all email adresses: 

````
def replace_domain(email, old_domain, new_domain):
    if '@' + old_domain in email:
        index=email.index("@"+old_domain)
        mew_email=old_email[:index]+"@"+new_domain
        return new_email
    return email # if email does not containe the # old domain just return the email as itself 
    
````
![str_16](images/str_16.png)   



