import random
import string
import heapq

POPULATION_SIZE = 1000
GENERATIONS = 200
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.1

def initialize_population():
    return [random.sample(string.ascii_uppercase, 26) for _ in range(POPULATION_SIZE)]

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        valid_words = set(word.strip().lower() for word in file)
    return valid_words

def load_special_words(file_path=None):
    if file_path:
        with open(file_path, 'r') as file:
            special_words = set(word.strip().lower() for word in file)
    else:
        special_words = {"babbage", "lovelace", "palmerstone", "ada", "charles", "lord"}
    return special_words

def load_text_from_file(file_path):
    if file_path:
        with open(file_path, 'r') as file:
            cipher_text = file.read()
            text = ''.join(filter(str.isalpha, cipher_text)).upper()
            # text = file.read().replace("\n", "").replace("\r", "").strip().lower()
    return text

def decrypt(ciphertext, alphabet):
    decrypt_dict = str.maketrans(string.ascii_uppercase, ''.join(alphabet))
    return ciphertext.translate(decrypt_dict)

def word_segmentation(text):
    cleaned_text = ''.join(char for char in text.lower() if char in string.ascii_lowercase)
    n = len(cleaned_text)
    dp = [None] * (n + 1)
    dp[0] = []

    for i in range(1, n + 1):
        for j in range(i):
            word = cleaned_text[j:i]
            if word in special_words and dp[j] is not None:
                if dp[i] is None or len(dp[j]) + 1 < len(dp[i]):
                    dp[i] = dp[j] + [word]
            elif word in valid_words and dp[j] is not None:
                if dp[i] is None or len(dp[j]) + 1 < len(dp[i]):
                    dp[i] = dp[j] + [word]

    return dp[n] if dp[n] is not None else []

def fitness_function(decrypted_text):
    # words = decrypted_text.split()
    if not decrypted_text:
        return 0 
    match_count = sum(1 for word in decrypted_text if word.lower() in special_words or valid_words)
    return match_count #/ len(decrypt_text)

def select(population, fitness_scores):
    elite_index = fitness_scores.index(max(fitness_scores))
    return [population[elite_index]] + random.choices(
        population, weights=fitness_scores, k=1
    )

def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1, 25)
        child1 = parent1[:crossover_point] + [c for c in parent2 if c not in parent1[:crossover_point]]
        child2 = parent2[:crossover_point] + [c for c in parent1 if c not in parent2[:crossover_point]]
        return child1, child2
    return parent1[:], parent2[:]

def mutate(alphabet):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(26), 2)
        alphabet[i], alphabet[j] = alphabet[j], alphabet[i]
    return alphabet

def genetic_algorithm():
    population = initialize_population()
    print(population[:5])
    best_fitness_history = []
    
    for generation in range(GENERATIONS):
        fitness_scores = [fitness_function(decrypt(ciphertext, alphabet)) for alphabet in population]
        best_fit = max(fitness_scores)
        best_fitness_history.append(best_fit)
        
        if len(best_fitness_history) > 20 and best_fitness_history[-1] == best_fitness_history[-20]:
            break
        
        best_individual = population[fitness_scores.index(best_fit)]
        
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = select(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            if len(new_population) < POPULATION_SIZE:
                new_population.append(mutate(child2))
        
        population = new_population

    if generation % 10 == 0: 
        print(f"Generation {generation}, Best Fitness: {best_fit}")

    best_individual = population[fitness_scores.index(max(fitness_scores))]
    return ''.join(best_individual), decrypt(ciphertext, best_individual)


dictionary_path= "/usr/share/dict/words"
special_words_path= "special_words.txt"
text_path = "ga_test.txt"

valid_words = load_dictionary(dictionary_path)
special_words = load_special_words(special_words_path)
text = load_text_from_file(text_path)


print("generation one")
print(fitness_function(['mr','charles','babbage','investigates','warne','lovelace','horsley']))
print("==============")

population=[]
fitness_history = []

population = initialize_population()
print(population[:10])

for decoding_alphabet in population:

    decrypt_text = decrypt(text[:100], decoding_alphabet)
    segmentation_text = word_segmentation(decrypt_text)
    fitness = fitness_function(segmentation_text)
    fitness_history.append(fitness)
    # if fitness < 70:
    #     print(decrypt_text)
    #     print(segmentation_text)
    #     print(fitness)
    

maxes = heapq.nlargest(2, fitness_history)
elite_index0 = fitness_history.index(maxes[0])
elite_index1 = fitness_history.index(maxes[1])

parent1 = population[elite_index0]
parent2 = population[elite_index1]

print("generation two")
print(fitness_function(['mr','charles','babbage','investigates','warne','lovelace','horsley']))
print("==============")

population=[]
fitness_history = []

for x in range(1000):
    population.extend(crossover(parent1, parent2))

print(population[:10])

for decoding_alphabet in population:

    decrypt_text = decrypt(text[:100], decoding_alphabet)
    segmentation_text = word_segmentation(decrypt_text)
    fitness = fitness_function(segmentation_text)
    fitness_history.append(fitness)
    if fitness < 90:
        print(decrypt_text)
        print(segmentation_text)
        print(fitness)   

maxes = heapq.nlargest(2, fitness_history)
elite_index0 = fitness_history.index(maxes[0])
elite_index1 = fitness_history.index(maxes[1])

parent1 = population[elite_index0]
parent2 = population[elite_index1]


print("generation three")
print(fitness_function(['mr','charles','babbage','investigates','warne','lovelace','horsley']))
print("==============")

population=[]
fitness_history = []

for x in range(1000):
    population.extend(crossover(parent1, parent2))

print(population[:10])

for decoding_alphabet in population:

    decrypt_text = decrypt(text[:100], decoding_alphabet)
    segmentation_text = word_segmentation(decrypt_text)
    fitness = fitness_function(segmentation_text)
    fitness_history.append(fitness)
    if fitness < 90:
        print(decrypt_text)
        print(segmentation_text)
        print(fitness)   

maxes = heapq.nlargest(2, fitness_history)
elite_index0 = fitness_history.index(maxes[0])
elite_index1 = fitness_history.index(maxes[1])

parent1 = population[elite_index0]
parent2 = population[elite_index1]

# best_alphabet, decoded_text = genetic_algorithm()
# print("Best alphabet found:", best_alphabet)
# print("Decoded text:", decoded_text[:100])  
