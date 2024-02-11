# total=['JAVA','PYTHON','JAVASCRIPT','HTML','CSS','DJANGO','CPP','MONGODB','PHP','NODEJS','REACT','ANGULARJS','DSA','FLASK','MYSQL']
# print("'],skills_dict['".join(total))
import matplotlib.pyplot as plt
import sqlite3
connection=sqlite3.connect('Customers.db')
cursor = connection.cursor()

def graph(list1,list2,skills,employees):
    def calculate_matching_percentage(dict1, list2):

        
        matching_count=0
        for i in list1:
            if i in set(list2):
                matching_count+=1
        matching_percentage = (matching_count / len(list1)) * 100
        print(list2,list1)
        if matching_percentage<70:
            matching_percentage=70
        return matching_percentage

    # list_a = [1, 2, 3, 4, 5]
    # list_b = [1, 2, 7, 4, 9]

    matching_percentage = calculate_matching_percentage(list1, list2)

    # Visualization as a shaded circle with the percentage value inside
    fig, ax = plt.subplots()
    circle_color = 'green'
    ax.pie([matching_percentage, 100 - matching_percentage], labels=['', ''], colors=[circle_color, 'lightgray'],
        autopct=lambda p: f'{matching_percentage:.2f}%' if p == 0 else '', startangle=90, wedgeprops=dict(width=0.4))

    # Draw a white circle at the center to make it look like a shaded circle
    centre_circle = plt.Circle((0, 0), 0.2, color='white', edgecolor='black', linewidth=0.8)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Add bold percentage text inside the circle
    ax.text(0, 0, f'{matching_percentage:.2f}%', ha='center', va='center', fontsize=12, color=circle_color, fontweight='bold')

    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('Matching Percentage between Two Lists')
    plt.savefig('static/matching.png')
    plt.close()

    # Sample data
    # employees = [emp[1] for emp in list2]
    

    # Create a bar graph
    plt.bar(employees, skills, color='blue')

    # Add labels and title
    plt.xlabel('Employees')
    plt.ylabel('Matching skills')
    plt.title('Individual contribution to the skills')
    plt.savefig('static/individual.png')
    plt.close()