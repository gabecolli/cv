skills = ["python", "Azure", "A+", "Azure Infrastructure", "Excel"]
updated_skills = []
for skill in skills:
    
    with open("skills.txt", "a") as file:
        file.write(f"<tr><td>{skill}</td><td>&#11088 &#11088 &#11088 &#11088 &#11088</td></tr>")


