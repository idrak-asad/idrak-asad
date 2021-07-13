import pandas as pd
print(1)
boyler_fitup=pd.read_excel("FITUP2.xlsx",sheet_name="BOILER",usecols = "C,G,H,O")
print(2)
print(boyler_fitup.head())


list_1199M326=[]
list_1200M326=[]
list_1201M326=[]

list_1199M321=[]
list_1200M321=[]
list_1201M321=[]

list_1199M325=[]
list_1200M325=[]
list_1201M325=[]

list_1199M320=[]
list_1200M320=[]
list_1201M320=[]

list_1199M316=[]
list_1200M316=[]
list_1201M316=[]


list_1199M326_2=[]
list_1200M326_2=[]
list_1201M326_2=[]

list_1199M321_2=[]
list_1200M321_2=[]
list_1201M321_2=[]

list_1199M325_2=[]
list_1200M325_2=[]
list_1201M325_2=[]

list_1199M320_2=[]
list_1200M320_2=[]
list_1201M320_2=[]

list_1199M316_2=[]
list_1200M316_2=[]
list_1201M316_2=[]


for i in range(len(boyler_fitup)):
    #print(i)
    list_tiny=[]
    list_tiny2=[]
    if boyler_fitup.iloc[i, 0]=="1199-M-326":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1199M326_2.append(list_tiny2)
        list_1199M326.append(list_tiny)
        
        
    elif boyler_fitup.iloc[i, 0]=="1200-M-326":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1200M326_2.append(list_tiny2)
        list_1200M326.append(list_tiny)

    elif boyler_fitup.iloc[i, 0]=="1201-M-326":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1201M326_2.append(list_tiny2)
        list_1201M326.append(list_tiny)

    elif boyler_fitup.iloc[i, 0]=="1199-M-321":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1199M321_2.append(list_tiny2)
        list_1199M321.append(list_tiny)

    elif boyler_fitup.iloc[i, 0]=="1200-M-321":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1200M321_2.append(list_tiny2)
        list_1200M321.append(list_tiny)

    elif boyler_fitup.iloc[i, 0]=="1201-M-321":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1201M321_2.append(list_tiny2)
        list_1201M321.append(list_tiny)

    elif boyler_fitup.iloc[i, 0]=="1199-M-325":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1199M325_2.append(list_tiny2)
        list_1199M325.append(list_tiny)

    elif boyler_fitup.iloc[i, 0]=="1200-M-325":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1200M325_2.append(list_tiny2)
        list_1200M325.append(list_tiny)

    elif boyler_fitup.iloc[i, 0]=="1201-M-325":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1201M325_2.append(list_tiny2)
        list_1201M325.append(list_tiny)

    elif boyler_fitup.iloc[i, 0]=="1199-M-320":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1199M320_2.append(list_tiny2)
        list_1199M320.append(list_tiny)

    elif boyler_fitup.iloc[i, 0]=="1200-M-320":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1200M320_2.append(list_tiny2)
        list_1200M320.append(list_tiny)

    elif boyler_fitup.iloc[i, 0]=="1201-M-320":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1201M320_2.append(list_tiny2)
        list_1201M320.append(list_tiny)

    elif boyler_fitup.iloc[i, 0]=="1199-M-316":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1199M316_2.append(list_tiny2)
        list_1199M316.append(list_tiny)

    elif boyler_fitup.iloc[i, 0]=="1200-M-316":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1200M316_2.append(list_tiny2)
        list_1200M316.append(list_tiny)

    elif boyler_fitup.iloc[i, 0]=="1201-M-316":
        list_tiny.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1])+"-F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny2.append(str(boyler_fitup.iloc[i, 1]))
        list_tiny2.append("F"+str(boyler_fitup.iloc[i, 2]))
        list_tiny.append(boyler_fitup.iloc[i, 3])
        list_1201M316_2.append(list_tiny2)
        list_1201M316.append(list_tiny)


df_1199M326=pd.DataFrame(list_1199M326,columns=['Seet_Joint',"1199-M-326-fit"])
df_1200M326=pd.DataFrame(list_1200M326,columns=['Seet_Joint',"1200-M-326-fit"])
df_1201M326=pd.DataFrame(list_1201M326,columns=['Seet_Joint',"1201-M-326-fit"])

df_1199M321=pd.DataFrame(list_1199M321,columns=['Seet_Joint',"1199-M-321-fit"])
df_1200M321=pd.DataFrame(list_1200M321,columns=['Seet_Joint',"1200-M-321-fit"])
df_1201M321=pd.DataFrame(list_1201M321,columns=['Seet_Joint',"1201-M-321-fit"])

df_1199M325=pd.DataFrame(list_1199M325,columns=['Seet_Joint',"1199-M-325-fit"])
df_1200M325=pd.DataFrame(list_1200M325,columns=['Seet_Joint',"1200-M-325-fit"])
df_1201M325=pd.DataFrame(list_1201M325,columns=['Seet_Joint',"1201-M-325-fit"])

df_1199M320=pd.DataFrame(list_1199M320,columns=['Seet_Joint',"1199-M-320-fit"])
df_1200M320=pd.DataFrame(list_1200M320,columns=['Seet_Joint',"1200-M-320-fit"])
df_1201M320=pd.DataFrame(list_1201M320,columns=['Seet_Joint',"1201-M-320-fit"])

df_1199M316=pd.DataFrame(list_1199M316,columns=['Seet_Joint',"1199-M-316-fit"])
df_1200M316=pd.DataFrame(list_1200M316,columns=['Seet_Joint',"1200-M-316-fit"])
df_1201M316=pd.DataFrame(list_1201M316,columns=['Seet_Joint',"1201-M-316-fit"])


df_326=pd.merge(df_1199M326, df_1200M326, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_326=pd.merge(df_326, df_1201M326, how="outer", on=["Seet_Joint", "Seet_Joint"])
print(df_326)

df_321=pd.merge(df_1199M321, df_1200M321, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_321=pd.merge(df_321, df_1201M321, how="outer", on=["Seet_Joint", "Seet_Joint"])
print(df_321)

df_325=pd.merge(df_1199M325, df_1200M325, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_325=pd.merge(df_325, df_1201M325, how="outer", on=["Seet_Joint", "Seet_Joint"])
print(df_325)

df_320=pd.merge(df_1199M320, df_1200M320, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_320=pd.merge(df_320, df_1201M320, how="outer", on=["Seet_Joint", "Seet_Joint"])
print(df_320)

df_316=pd.merge(df_1199M316, df_1200M316, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_316=pd.merge(df_316, df_1201M316, how="outer", on=["Seet_Joint", "Seet_Joint"])
print(df_316)

list_1199M326b=[]
list_1200M326b=[]
list_1201M326b=[]

list_1199M321b=[]
list_1200M321b=[]
list_1201M321b=[]

list_1199M325b=[]
list_1200M325b=[]
list_1201M325b=[]

list_1199M320b=[]
list_1200M320b=[]
list_1201M320b=[]

list_1199M316b=[]
list_1200M316b=[]
list_1201M316b=[]

boyler_log=pd.read_excel("BOILER_LOG.xlsx",sheet_name="Boiler_Log",usecols = "B,D,Y,AA,AB,AD")
print("Boyler log")
print(boyler_log.head())


for i in range(len(boyler_log)):
    list_tiny=[]
    if boyler_log.iloc[i, 0]=="1199-M-326":
    
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1199M326b.append(list_tiny)
        
    elif boyler_log.iloc[i, 0]=="1200-M-326":
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1200M326b.append(list_tiny)

    elif boyler_log.iloc[i, 0]=="1201-M-326":
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1201M326b.append(list_tiny)

    elif boyler_log.iloc[i, 0]=="1199-M-321":
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1199M321b.append(list_tiny)

    elif boyler_log.iloc[i, 0]=="1200-M-321":
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1200M321b.append(list_tiny)

    elif boyler_log.iloc[i, 0]=="1201-M-321":
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1201M321b.append(list_tiny)


asme_log=pd.read_excel("BOILER_LOG.xlsx",sheet_name="ASME_PIPE",usecols = "C,E,W,Z,AA,AC")
print("Asme Log")
print(asme_log.head())

for i in range(len(asme_log)):
    list_tiny=[]
    if asme_log.iloc[i, 0]=="1199-M-325":
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1199M325b.append(list_tiny)

    elif asme_log.iloc[i, 0]=="1200-M-325":
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1200M325b.append(list_tiny)

    elif asme_log.iloc[i, 0]=="1201-M-325":
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1201M325b.append(list_tiny)

    elif asme_log.iloc[i, 0]=="1199-M-320":
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1199M320b.append(list_tiny)

    elif asme_log.iloc[i, 0]=="1200-M-320":
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1200M320b.append(list_tiny)

    elif asme_log.iloc[i, 0]=="1201-M-320":
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1201M320b.append(list_tiny)

    elif asme_log.iloc[i, 0]=="1199-M-316":
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1199M316b.append(list_tiny)

    elif asme_log.iloc[i, 0]=="1200-M-316":
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1200M316b.append(list_tiny)

    elif asme_log.iloc[i, 0]=="1201-M-316":
        list_tiny.append(str(boyler_log.iloc[i, 1])+"-"+str(boyler_log.iloc[i, 2]))
        list_tiny.append(boyler_log.iloc[i, 4])
        list_tiny.append(boyler_log.iloc[i, 3])
        list_tiny.append(boyler_log.iloc[i, 5])
        list_1201M316b.append(list_tiny)


df_1199M326b=pd.DataFrame(list_1199M326b,columns=['Seet_Joint',"1199-M-326-b", "1199-WPS","1199-Welder"])
df_1200M326b=pd.DataFrame(list_1200M326b,columns=['Seet_Joint',"1200-M-326-b", "1200-WPS","1200-Welder"])
df_1201M326b=pd.DataFrame(list_1201M326b,columns=['Seet_Joint',"1201-M-326-b", "1201-WPS","1201-Welder"])

df_1199M321b=pd.DataFrame(list_1199M321b,columns=['Seet_Joint',"1199-M-321-b", "1199-WPS","1199-Welder"])
df_1200M321b=pd.DataFrame(list_1200M321b,columns=['Seet_Joint',"1200-M-321-b", "1200-WPS","1200-Welder"])
df_1201M321b=pd.DataFrame(list_1201M321b,columns=['Seet_Joint',"1201-M-321-b", "1201-WPS","1201-Welder"])

df_1199M325b=pd.DataFrame(list_1199M325b,columns=['Seet_Joint',"1199-M-325-b", "1199-WPS","1199-Welder"])
df_1200M325b=pd.DataFrame(list_1200M325b,columns=['Seet_Joint',"1200-M-325-b", "1200-WPS","1200-Welder"])
df_1201M325b=pd.DataFrame(list_1201M325b,columns=['Seet_Joint',"1201-M-325-b", "1201-WPS","1201-Welder"])

df_1199M320b=pd.DataFrame(list_1199M320b,columns=['Seet_Joint',"1199-M-320-b", "1199-WPS","1199-Welder"])
df_1200M320b=pd.DataFrame(list_1200M320b,columns=['Seet_Joint',"1200-M-320-b", "1200-WPS","1200-Welder"])
df_1201M320b=pd.DataFrame(list_1201M320b,columns=['Seet_Joint',"1201-M-320-b", "1201-WPS","1201-Welder"])

df_1199M316b=pd.DataFrame(list_1199M316b,columns=['Seet_Joint',"1199-M-316-b", "1199-WPS","1199-Welder"])
df_1200M316b=pd.DataFrame(list_1200M316b,columns=['Seet_Joint',"1200-M-316-b", "1200-WPS","1200-Welder"])
df_1201M316b=pd.DataFrame(list_1201M316b,columns=['Seet_Joint',"1201-M-316-b", "1201-WPS","1201-Welder"])


df_326=pd.merge(df_326, df_1199M326b, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_326=pd.merge(df_326, df_1200M326b, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_326=pd.merge(df_326, df_1201M326b, how="outer", on=["Seet_Joint", "Seet_Joint"])
print(df_326)

df_321=pd.merge(df_321, df_1199M321b, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_321=pd.merge(df_321, df_1200M321b, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_321=pd.merge(df_321, df_1201M321b, how="outer", on=["Seet_Joint", "Seet_Joint"])
print(df_321)

df_325=pd.merge(df_325, df_1199M325b, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_325=pd.merge(df_325, df_1200M325b, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_325=pd.merge(df_325, df_1201M325b, how="outer", on=["Seet_Joint", "Seet_Joint"])
print(df_325)

df_320=pd.merge(df_320, df_1199M320b, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_320=pd.merge(df_320, df_1200M320b, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_320=pd.merge(df_320, df_1201M320b, how="outer", on=["Seet_Joint", "Seet_Joint"])
print(df_320)

df_316=pd.merge(df_316, df_1199M316b, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_316=pd.merge(df_316, df_1200M316b, how="outer", on=["Seet_Joint", "Seet_Joint"])
df_316=pd.merge(df_316, df_1201M316b, how="outer", on=["Seet_Joint", "Seet_Joint"])
print(df_316)


def count_funk(data):
    i=pd.Series(data)
    tiny_count=[]
    count=0
    fitup=str(i.iloc[1])
    boyler=str(i.iloc[4])
    if len(fitup)!=len(boyler):
        count+=1
    fitup=str(i.iloc[2])
    boyler=str(i.iloc[7])
    if len(fitup)!=len(boyler):
        count+=1
    fitup=str(i.iloc[3])
    boyler=str(i.iloc[10])
    if len(fitup)!=len(boyler):
        count+=1
    tiny_count.append(i.iloc[0])
    tiny_count.append(count)
    return tiny_count

ls326_count=[]
for i in df_326.values:
    tiny_count=count_funk(i)
    ls326_count.append(tiny_count)
df_count=pd.DataFrame(ls326_count, columns=["Seet_Joint","Count"])
print(df_count)
df_326=pd.merge(df_326, df_count, how="outer", on=["Seet_Joint", "Seet_Joint"])

ls321_count=[]
for i in df_321.values:
    tiny_count=count_funk(i)
    ls321_count.append(tiny_count)
df_count=pd.DataFrame(ls321_count, columns=["Seet_Joint","Count"])
print(df_count)
df_321=pd.merge(df_321, df_count, how="outer", on=["Seet_Joint", "Seet_Joint"])
'''
ls325_count=[]
for i in df_325.values:
    tiny_count=count_funk(i)
    ls325_count.append(tiny_count)
df_count=pd.DataFrame(ls325_count, columns=["Seet_Joint","Count"])
print(df_count)
df_325=pd.merge(df_325, df_count, how="outer", on=["Seet_Joint", "Seet_Joint"])

ls320_count=[]
for i in df_320.values:
    tiny_count=count_funk(i)
    ls320_count.append(tiny_count)
df_count=pd.DataFrame(ls320_count, columns=["Seet_Joint","Count"])
print(df_count)
df_320=pd.merge(df_320, df_count, how="outer", on=["Seet_Joint", "Seet_Joint"])

ls316_count=[]
for i in df_316.values:
    tiny_count=count_funk(i)
    ls316_count.append(tiny_count)
df_count=pd.DataFrame(ls316_count, columns=["Seet_Joint","Count"])
print(df_count)
df_316=pd.merge(df_316, df_count, how="outer", on=["Seet_Joint", "Seet_Joint"])

'''

df_326.to_excel ("BOYLER CONTROL 326.xlsx",sheet_name="326", index = False, header=True)

df_321.to_excel ("BOYLER CONTROL 321.xlsx",sheet_name="321", index = False, header=True)

df_325.to_excel ("BOYLER CONTROL 325.xlsx",sheet_name="325", index = False, header=True)

df_320.to_excel ("BOYLER CONTROL 320.xlsx",sheet_name="320", index = False, header=True)

df_316.to_excel ("BOYLER CONTROL 316.xlsx",sheet_name="316", index = False, header=True)