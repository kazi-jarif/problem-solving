qus=["1.Which is the largest ocean on Earth?\nA) Atlantic Ocean       B) Pacific Ocean","\n2. Which is the longest river in the world?\nA) Nile River       B) Amazon River","\n3. Which gas do plants absorb from the atmosphere during photosynthesis?\nA) Oxygen      B) Carbon Dioxide","\n4. Which is the smallest continent in the world by land area?\nA) Australia      B) Europe","\n5.Who is known as the Father of the Nation in India?\nA) Mahatma Gandhi       B) Jawaharlal Nehru","\n6. Which planet in our solar system is known as the Red Planet?\nA) Venus      B) Mars","\n7. What is the capital city of Japan?\nA) Beijing       B) Tokyo","\n8. Which element has the chemical symbol 'O'?\nA) Oxygen       B) Gold","9\n. Which animal is known as the Ship of the Desert?\nA) Elephant       B) Camel","\n10. How many sides does a hexagon have?\nA) 6       B) 8"]
ans=['B','A','B','A','A','B','B','A','B','A']
total=0
for i in qus:
    print(i)
    for j in ans:
        inpu=input("your answer(A/B): ")
        upinpu=inpu.upper()
        if j==upinpu:
            print("your correct")
            total=total+1000
            ans.pop(0)
            break
        else:
            print("your wrong")
            ans.pop(0)
            break
print("your total income",total)
    