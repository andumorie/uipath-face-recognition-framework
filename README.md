# Instructions

1. Install Python (including pip) using the provided installation kit in the Prerequisites folder
2. Add the Python paths to your PATH system environment variable (You can find your PATH variable by going to My Computer > Properties > Advanced System Settings > Environment Variables > System Variables > Path). Click on Edit and add the following paths, replacing "YOUR_USERNAME" with your Windows username:
    - C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python36
    - C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python36\Scripts
3. Run install.bat in the Prerequisites folder
4. Update the Python path in the Config.xlsx with your Python path (C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python36).
5. Create a project in AI Center
6. Create a dataset and make it public
7. Create assets in Orchestrator for the dataset endpoint/APIKey and update Config.xlsx file
8. Run Main-UploadDataset.xaml file to populate dataset in AI Centre
7. Upload custom ML Package in the AIC project. You can find the package here https://github.com/danielepassos-ui/uipath-face-recognition-mlpackage
    - Follow instructions in the ML Package repository to create the MK Skill
8. Create assets in Orchestrator for the MKSkill endpoint/APIKey and update Config.xlsx file, when the MLSkill is made public and available
9. Run Main-Identify.xaml to identify someone
