choice=input ("L,D,B");
if(choice=="B"):
    food=input("SI or NI");
    if(food=="SI"):
        c=input("idle or dosa");
        if(c=="idle"):
            print("you ordered idle");
if(choice=="L"):
    food=input("Punjabi or bihari");
    if(food=="bihari"):
        c=input("chole or littee chokha");
        if(c=="chole"):
            print("you ordered chole");
if (choice=="D"):
    food=input("maharashtrian or gujrati");
    if(food=="maharashtrian"):
        c=input("rajma chawal or biryani");
        if(c=="biryani"):
            print("you ordered biryani");