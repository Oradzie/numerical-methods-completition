with open("scheletri.txt", "r") as file:
    scheletri = file.read().splitlines()

folder = "methods/"
method = ""
file_name = ""    
solutions = []

for line in scheletri:
    
    if "def" in line:
        
        if len(solutions) > 0:
            with open(f"{folder}{file_name}", "a") as file:
                for solution in solutions:
                    file.write(f"\n# {solution}")
            solutions = []

        method = line.split('def')[1].split('(')[0].strip()
        file_name = f"{method}.txt"

        with open(f"{folder}{file_name}", "w") as file:
            file.write(line)

        print(f"Created file {file_name} and wrote first line")
    else:
        if "# added" in line:
            line = line.replace("# added", "")
            clean_line = line.strip()
            if "while" == clean_line.split(" ")[0]:
                clean_line = clean_line.split("while")[1].strip()
            if ":" == clean_line[-1]:
                clean_line = clean_line.split(":")[0].strip()
            if "if" == clean_line.split(" ")[0]:
                clean_line = clean_line.split("if")[1].strip()
            if "=" == clean_line.split(" ")[1]:
                clean_line = clean_line.split(" = ")[1].strip()
            
            solutions.append(clean_line)
            
            with open(f"{folder}{file_name}", "a") as file:
                file.write(f"\n{line.replace(clean_line, '___')}")
        else:            
            with open(f"{folder}{file_name}", "a") as file:
                file.write(f"\n{line}")

if len(solutions) > 0:
    with open(f"{folder}{file_name}", "a") as file:
        for solution in solutions:
            file.write(f"\n# {solution}")
    solutions = []