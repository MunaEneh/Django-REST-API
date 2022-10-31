# Week 6 Python Task: Django REST Framework
 
Build a simple REST API to list all the songs in our database and all the artists. Your API should also be able to fetch a particular song, delete and update a particular song.Push your code to the same GitHub repository
 
Note:  When you delete a particular song in the API, All lyrics of that song should be deleted. Also, updating a song simply means updating the song title or the date it was published
 
## TASK EXPLANATION
<li> This task was done in Vscode.</li>
<li> Before you open VScode, you create a folder in your desktop. All files would be automatically saved in this folder.</li>
<li> Make Sure that the python extension is installed in VScode.</li>
<li> Open a new terminal, and create a virtual environment, you can give this virtual environment any name. The name of my virtual environment in this repo is "Zuri-django-project".</li>
<li> It is in this virtual environment that you install django.</li>
<li> Open a file in your workspace and name the file requirements.txt. It is in this file that you will pin all your dependencies.The dependencies are softwares required for your django project to run or work effectively. To pin these dependencies, simply type them into your requirements.txt file and assign their version using the "==" symbol. to check if the request has been satisfied. type the code "py -m pip install -r requirements.txt".</li>
<li>This code will make sure all the required dependencies have been installed. if they have been installed, your terminal will show you that the request has already been satisfied.</li>
<li> In your "musicapp" folder. Go to "models.py", open it. In this file you will fulfill the requirements by creating three models and giving them the attributes ascribed to them. For instance , the model artiste has the attribute (first_name, last_name, age).</li>
<li> In the "songcrud" folder, go to "settings.py", under installed apps, type "musicapp". Finally, you were told to find the key relationship between the three models and use foreignkey to specify this relationship. The relationship is Many to 1, which as already been hinted at by the use of the word ""foreignkey.</li>
<li> After all this , you move to the “musicapp” folder, and click on the “admin.py”. Here, you will register all your models. My models are (Artiste, Song, Lyrics). </li>
<li> Now, in your terminal, you have to create a superuser, it is in this super user that you will set up your login info. All the info you put here will be used to access the admin page on your django.</li>
<li> To access and see the admin page. Type “py manage.py runserver”. When you click on the link which looks like this “http://127.0.0.1:8000/”. You will see that your django is successful. Now, to see the admin add “/admin” to the link. This will give you “http://127.0.0.1:8000/admin/” . This page will be a login page.</li>
<li> Now, enter all the info that you supplied to the superuser on your terminal in VScode. This should open your admin. </li>
<li> Now, let's look at the contents of each model that I registered. The Artiste model will show you a list of Artiste that I have entered into the database. The artists that I added are : Buju, Rihanna, and Beyonce.</li> To add another artist, click the “add artiste ” button that is underlined in red.
<li> Ihave populated the Lyrics and Song databases with data too.
 
#### NOTE: it is advisable to populate your database first before you start to work on it. This is because you can test your database easier when it is already populated.
 
<li> The task required that I build a simple REST API. to do this, I installed the djangorestframework in my VScode. You do this by typing “pip install djangorestframework” in your terminal.</li>
<li>In my “musicapp” folder, I created a file called “serializers.py” then i populate it with code that would allow me arrange my data. </li>
<li> You also have to populate the “views.py” file in your “musicapp” folder. It is in this views.py that you will enter the codes that list the songs in your database. To get the list of songs in your database , you use GET.
<li> To test my API,  I had to download <b>Thunderclient</b>. It is an extension on <b>VScode</b>. It allows you to test your API. They are other API testing software like <b>Postman</b>. But I prefered to use one that I could operate on VScode, so that I would not have to leave VScode and go to my browser.</li>
<li> To test the API, you migrate using “py manage.py migrate” before you “runserver”.</li>
<li> After you runserver, copy the link and paste on your <b>Thunderclient</b> terminal.</li>
<li> In Thunderclient, we are using the GET commnd. This command has listed all the artists that I have in my database. I have 5 artists in my protocol and the GET command has listed all these artists. GET will always show the list of artistes, songs or lyrics in my database. It all depends on the link you post. “http://127.0.0.1:8000/musicapp/” will show you a list of Artists in the database. “http://127.0.0.1:8000/musicapp2/” will give you the list of songs in my database. “http://127.0.0.1:8000/musicapp3/” will show you the list of Lyrics. These links are only accessible in my database. I used my “urls.py” file to create these paths. 
<li> Even without thunderclient, you can view this in normal browser by using the links, just as they were mentioned, since I am trying to see the list of artist in my database, I will use the “http://127.0.0.1:8000/musicapp/” link.</li>
<li> By doing this, I have satisfied the first requirement for this task, I have listed the artists in my database using the  <b>GET command</b>.</li> 
<li> Even without Thunderclient, we can view the list of songs in our database using the link “http://127.0.0.1:8000/musicapp2/”. </li>
<li> With this we have satisfied the first requirement which says “Build a simple REST API to list all the songs in our database and all the artists”.</li>
<li> Now, my API should be able to select one song. To do this you have to define a new path in your “urls.py” file. And also add code to your “views.py” in order to display this change. I did this and created the “http://127.0.0.1:8000/musicapp2/1” link. The GET command is used to fetch a particular song too. This link will select or fetch a particular song in my API.</li>
<li> To delete a particular song, you use the DELETE command. In my database, I used the DELETE command to delete the 5th song in my database. For this you use the "http://127.0.0.1:8000/musicapp2/5" with the <b>DELETE command</b>. </li>
<li> To make sure that song 5 has been deleted, you make use of the <b>GET</b> command. Run the <b>GET</b> command with the “http://127.0.0.1:8000/musicapp2/” link. This link will show the present list of songs in the database ; but now , song 5 would not be part of the database.</li>
<li> The name of the song that was deleted was <b>Diamond by Rihanna</b> and it is no longer in my database. It has been deleted using the <b>DELETE</b> command.</li>
<li> Since the song was deleted from the database, the lyrics for that song had to be deleted too. This was automatic. When a song is deleted, the lyrics are deleted too.</li>
<li> To update a song, we can change either the title or date-released of a song. I updated the song using the <b>PUT</b> command. Below, you will see the picture showing that a song was selected.</li>
<li> In my API, the song “Brown Skin girl ” will be changed to “Halo”.</li>
 
#### The requirements of the tasks were satisfied.
<li> My API listed all the songs and artists in the database using the GET command.</li>
<li> In my API, you can select a particular song using the GET command to wit the index [1 to(the total of songs available)].</li>
<li> In my API, you can also update a particular song, using the PUT command.</li>
<li> You can add songs, artistes and lyrics to any of the databases using the POST command.</li>
<li> The DELETE command is used to delete a particular song in the database.</li>
<li> I used the GET command to check if all these commands had made changes to my databases.</li> 
<li> I tested my API in Thunderclient. It is a VScode extension.</li> 
