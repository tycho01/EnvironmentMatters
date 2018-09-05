# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 22:53:46 2018

@author: Victor Zuanazzi
"""
import numpy as np
import matplotlib.pyplot as plt
import math

class Population():
    
    def __init__(self, size, dna_lengh, color):
        '''Creates a population'''
        self.dna_lengh = dna_lengh #number of genes of each individuo of the 
        #population.
        self.size = size #number of individuos in the population.
        self.color = color #color is used for ploting.
        self.fit = []#stores the fit score of each individuo.
        for i in range(size):
            self.fit.append(0)
        self.birth()
        
    def birth(self):
        '''Randomly creates individuos'''
        #All genes are picked from an uniform distribution between -1 and 1.
        self.genes = 2*np.random.random_sample((self.size, self.dna_lengh))-1
    
    def fit_function(self, environment):
        for j in range(self.size):
            fit = 0
            for i in range(self.dna_lengh):
                fit = fit + self.genes[j][i]*pow(environment, i)
            self.fit[j] = fit
            self.champion()

    def sex_op(self, son, mom):
        '''Effectively creates a new individuo based on two other.
        
        inputs:
            son: it is the individuo to be replaced. Its genes will be modified.
            mom: a second individuo that will be used for sexual reproductio.
        '''
        #The sex function is just a randomly weighet average of the individuo 
        #to be replaced and a better individuo.
        for j in range(self.dna_lengh):
            a = np.random.random_sample()
            self.genes[son][j] = (a*self.genes[son][j]+ (1-a)*self.genes[mom][j])
            if np.random.random_sample() > 0.95:
                #Mutation factor is kept at 5%.
                self.genes[son][j] = 2*np.random.random_sample()-1
    
    def champion(self):
        '''Finds the index of the best fit of the population'''
        self.best = self.fit.index(max(self.fit))
    
    def new_generation(self):
        '''Replaces the current generation with a new one.'''
        #Not optimal, but simple, combination of indiviuos for sexual reproduction.
        for i in range(self.size-2):
            if self.fit[i] < self.fit[i+1]:
                self.sex_op(i, i+1)
        #The last individuo is aways compared to the champion. 
        last = self.size-1
        if self.fit[last] < self.fit[self.best]:
            self.sex_op(last, self.best)
    
    def print_champion(self, message = ''):
        ''''Print fitness score and genes of the champion of the population.'''
        print(message, 'Champion Fit Score: ', self.fit[self.best])
        print(message, "Champion Genes:")
        print(self.genes[self.best])

    def print_all(self, message = ''):  
        ''''Print fitness score and genes of the all population.'''
        print(message, 'Fit Score: \n', self.fit)
        print(message, "Genes:")
        print(self.genes)

    def plot_fit(self, environment):
        '''Plots the fitness into a scatter graph.  '''
        env = list(map(lambda x: environment, self.fit))
        plt.scatter(env, self.fit, color= self.color)
        
def example():
    ''' This aims to show why environment matters in evolutionary computing.'''
    
    #Creates two populations to be comparared.
    population_1 = Population(100, 5, 'red')
    population_2 = Population(100, 5, 'blue')
    
    #Loop to optimize the each population to its envinronment.
    n_iterations = 100
    for i in range(n_iterations):
        #The environments are constant functions x = 1 and x = -1. Those two 
        #were chosen for the sake of simplicity.
        #Polulation 1 is in the environment x = 1. 
        population_1.fit_function(1)
        #Population 2 is in the environment x = -1.
        population_2.fit_function(-1)
        
        if i in list(range(0,n_iterations,10)):
            #Print the fit score and the genes best performers of both populations. 
            print('\n+++ Iteration ', i, ': +++')
            population_1.print_champion('Polulation 1')
            population_2.print_champion('Polulation 2')
        #Population is replaced by a better adapted population:
        population_1.new_generation()
        population_2.new_generation()
    
    #Print and plot findings by the end of the exercise.
    population_1.print_champion('Polulation 1')
    population_2.print_champion('Polulation 2')
    print('Fit Score of all individuos of all populations:')
    population_1.plot_fit(1)
    population_2.plot_fit(-1)
    

