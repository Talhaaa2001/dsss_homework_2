from setuptools import setup, find_packages

setup(
    name='math-quiz-game',
    version='3.0.0',
    packages=find_packages(),
    install_requires=[
        
        # Add any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'math-quiz=math_quiz.math_quiz:math_quiz',
        ],
    },
    
)