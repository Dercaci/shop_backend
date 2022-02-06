* To start the project please run: docker-compose up --build and acces the http://0.0.0.0:8000

* The full acces have only superusers and staff users, if you want to check how my code works you can to log in 
as administrator:
                login: vitalie
                password: 1234
or as a simple user with limited acces:
                login: user1
                password: 1234
    (the superusers or staff users have all the permisions, for example to see all the users on the site and all the wishlists)
    (the simple users have the permissions to create products and wishlists)
    (the anonymus users (who are not logged in) has only the permissions to see list of products and create a new user)

* Type of authentication: Base authentication


Se da un magazin cu o lista de produse.
Fiecare utilizator isi poate crea mai multe liste cu preferinte (wishlists)
Fiecare utilizator poate adauga produse in listele sale cu preferinte
Pentru fiecare produs din lista, trebuie sa fie aratat citi utilizatori unici au dorit acest produs (adaugat in wishlist)


Endpoints: 

1. CRUD pentru o lista de produse

2. CRUD pentru wishlists 

    
