storage={
            'id':{'E':["T","E'"],'T':["F","T'"],'F':["id"]},
            '+':{"E'":["+","T","E'"],'T':["synch"],"T'":['ε'],"F":['synch']},
            '*':{"T'":["*","F","T'"],'F':['synch']},
            '(':{'E':["T","E'"],'T':["F","T'"],'F':["(","E",')']},
            ")":{'E':['synch'],"E'":['ε'],'T':['synch'],"T'":['ε'],'F':['synch']},
            '$':{'E':["synch"],"E'":['ε'],'T':['synch'],"T'":['ε'],'F':['synch']}
         }

non_terminals=["E","E'","T","T'","F"]


stack=['$','E']
inp='id id++id'
tokens=[]
a=''

# creating tokens from input
for i in inp:
    if 'a'<i<'z' or 'A'<i<"Z":
        a+=i
    else:
        if a!='':
            if a!=' ':
                tokens.append(a)
        if i!='':
            if i!=' ':
             tokens.append(i)
        a=''
if a!='':
            if a!=' ':
                tokens.append(a)


# acual algorithm
while stack!=['$']:
    if tokens!=[]:                      #if string is being persed, look for its action

        if tokens[0] in storage.keys():          #if input token belongs to the table, then look for its productions 

            productions=storage.get(tokens[0])
            a=stack.pop()

            # if a=="'":                 #not necessary just in case if asked how will i handel '.
            #     a+=stack.pop()

            the_one=productions.get(a)
            
            if the_one==['synch']:          #if 'synch' then just pop the top of stack
                print(f'M[{a},{tokens[0]}] = synch\nhence, pop from stack\n')

            else:                          # if anything other then synch do appropriate actions

                if the_one:            # if theere production exists then enter
                    for i in range(len(the_one)-1,-1,-1):      #inserting the productions if only they are not 'ε'

                        if the_one[i]!='ε':
                            stack.append(the_one[i])

                    print(f'output: {a} -> {"".join(the_one)}\n')

                else:                  # if theere production does not exist then pop that token and keep the stack intact
                    out=tokens.pop(0)
                    stack.append(a)
                    print(f'M[{a},{out}] = blank\nhence, skip {out}\n')
                 
            if stack[-1] not in non_terminals:          #to check the terminals

                if stack[-1]==tokens[0]:                    # if top of stack and input tokens match then enter
                    print(f'match: {tokens[0]}\n')
                    tokens.pop(0)
                    stack.pop()

                else:                                       # if top of stack and input tokens do not match then pop the stack
                    found=stack.pop()
                    print(f'top of the stack [{found}] does not matchtop of the input [{tokens[0]}]\n')

        else:                #if input token dont belong to the table, skip that token
            tokens.pop(0)
           

        
    else:                   #if string is empty, look for how to end it in ''$'' production
        productions=storage.get('$')
        a=stack.pop()
        the_one=productions.get(a)
        
        if the_one==['synch']:          #if 'synch' then just pop the top of stack
            print(f'M[{a},{tokens[0]}] = synch\nhence, pop from stack\n')

        elif the_one==['ε']:
            print(f'output: {a} -> {"".join(the_one)}\n')

        else:
            for i in range(len(the_one)-1,-1,-1):      #inserting the productions if only they are not 'ε'
                        if the_one[i]!='ε':
                            stack.append(the_one[i])

if tokens!=[]:
     print(f'tokens left but stack is empty \nremaining tokens are "{" ".join(tokens)}"  ')
