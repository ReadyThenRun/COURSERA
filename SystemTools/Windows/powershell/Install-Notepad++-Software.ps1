
<#
.Synopsis
   Powershell DSC script to install NotepadPlusPlus exe file on any machine
.DESCRIPTION
   Powershell DSC script to install NotepadPlusPlus exe file on any machine
.NOTES    
    Name: Install-NotepadPlusPlusDSC.ps1
    Author: Deepak Vishwakarma
    Email : Deepitpro@outlook.com
    Version: 0.1 
    DateCreated: 04 Nov 2017
#>

Configuration InstallNotepadPlusPlus
{

Import-DscResource –ModuleName 'PSDesiredStateConfiguration'

Node Localhost #update the node name
    {
     #Notepad++
     Package NotepadPlusPlus
     {
     Ensure = 'Present'
     Name = 'Notepad++ (64-bit x64)'
     Path = 'D:\NotepadPlusPlus\npp.7.5.1.Installer.x64.exe' #update the file path
     ProductId = ''
     Arguments = '/S'
    }
    }
}
        


InstallNotepadPlusPlus -OutputPath C:\

Start-DscConfiguration -Path c:\ -Wait -Verbose -Force
