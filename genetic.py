import random
def genetic_algo(project_requirements,employees,team_size):
    print(employees)
    # employees = {
    #     'Employee1': {'Skill1': 1, 'Skill2': 0, 'Skill3': 1, 'Skill4': 0},
    #     'Employee2': {'Skill1': 0, 'Skill2': 0, 'Skill3': 1, 'Skill4': 0},
    #     'Employee3': {'Skill1': 0, 'Skill2': 1, 'Skill3': 1, 'Skill4': 0},
    #     'Employee4': {'Skill1': 1, 'Skill2': 1, 'Skill3': 0, 'Skill4': 0},
    #     'Employee5': {'Skill1': 0, 'Skill2': 1, 'Skill3': 1, 'Skill4': 0},
    #     'Employee6': {'Skill1': 1, 'Skill2': 0, 'Skill3': 1, 'Skill4': 0},
    # }

    # project_requirements = {'Skill1': 1, 'Skill2': 1, 'Skill3': 1, 'Skill4': 0}

    # Genetic algorithm parameters
    # team_size = 3
    population_size = 50
    num_generations = 100
    mutation_rate = 0.1
    
    # Define the individuals in the population
    def create_individual():
        # Randomly select employees for the team
        return random.sample(list(employees.keys()), team_size)

    # Define the fitness function
    def fitness(individual):
        # Calculate the fitness as the number of matching skills with project requirements
        matching_skills = sum(employees[employee][skill] for employee in individual for skill in project_requirements.keys())
        return matching_skills

    # Select individuals for the next generation based on their fitness
    def select(population):
        total_fitness = sum(fitness(ind) for ind in population)
        probabilities = [fitness(ind) / total_fitness for ind in population]
        return random.choices(population, weights=probabilities, k=population_size)

    # Crossover: Combine genetic information of two individuals
    def crossover(parent1, parent2):
        # Perform uniform crossover to maintain the team size
        child1 = [gene1 if random.random() < 0.5 else gene2 for gene1, gene2 in zip(parent1, parent2)]
        child2 = [gene1 if random.random() < 0.5 else gene2 for gene1, gene2 in zip(parent2, parent1)]
        return child1, child2

    # Mutation: Introduce random changes to an individual
    def mutate(individual):
        # Randomly swap an employee
        mutated_individual = individual.copy()
        index = random.randint(0, team_size - 1)
        available_employees = list(set(employees.keys()) - set(mutated_individual))
        mutated_individual[index] = random.choice(available_employees)
        return mutated_individual

    # Main genetic algorithm
    def genetic_algorithm():
        population = [create_individual() for _ in range(population_size)]

        for generation in range(num_generations):
            fitness_scores = [fitness(ind) for ind in population]

            selected_population = select(population)

            offspring = []
            for i in range(0, population_size, 2):
                parent1, parent2 = selected_population[i], selected_population[i + 1]
                child1, child2 = crossover(parent1, parent2)
                offspring.extend([mutate(child1), mutate(child2)])

            population = offspring

            best_individual = max(population, key=fitness)
            print(f"Generation {generation + 1}, Best Fitness: {fitness(best_individual)}")

        return list(set(max(population, key=fitness)))
    return genetic_algorithm()
# Example usage
if __name__=="__main__":
    best_team = genetic_algo(project_requirements = {'Skill1': 1, 'Skill2': 1, 'Skill3': 1, 'Skill4': 0})
    print("Best Team:", list(set(best_team)))
