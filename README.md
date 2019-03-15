1. Install Python (including pip) using the provided installation kit in the Prerequisites folder
2. Add the Python paths to your PATH system environment variable (You can find your PATH variable by going to My Computer > Properties > Advanced System Settings > Environment Variables > System Variables > Path). Click on Edit and add the following paths, replacing "YOUR_USERNAME" with your Windows username:
    - C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python36
    - C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python36\Scripts
3. Run install.bat in the Prerequisites folder
4. The previous batch script should've automatically created a config.csv file in the main project folder containing your machine's Python path, but be sure to check and manually edit it and put in your Python path (C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python36) if the workflow gives a Python error when running.
5. Run the framework from the Main.xaml workflow inside UiPath Studio
6. Customize the Process.xaml workflow to include your own process to be run after the face recognition