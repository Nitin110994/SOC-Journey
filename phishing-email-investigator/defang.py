url = input("Enter a URL to defang: ")
if "hxxp" in url:
    print("This URL is already defanged.")
else:
    defanged = url.replace("http", "hxxp")
    defanged= defanged.replace(".","[.]")
    print(defanged)