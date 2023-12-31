# ABOUT / INFO 
To access the movie recommendation site, please visit https://movie-recommendations-tm4e.onrender.com/ <br />

This application uses consine similarity to assign similarity scores between the inputted movie and the ones available within the database (constructed with MongoDB).
Movies that aren't available within the database are fetched using an API and specific information (such as cast, keywords, summary) and are added to the MongoDB database. <br />

The application uses HTML & CSS for the frontend, Node.js for the backend that calls a python script that runs the machine learning algorithm and produces a list of similar movies. 

