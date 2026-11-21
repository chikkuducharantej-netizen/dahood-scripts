; Inno Setup script for DaHood Scripts
#define AppName "DaHood Scripts"
#define AppVersion "1.4.2"
#define AppPublisher "dahood-scripts"

[Setup]
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#AppPublisher}
DefaultDirName={autopf}\DaHoodScripts
DefaultGroupName={#AppName}
OutputBaseFilename=dahood-scripts-setup
Compression=lzma2
SolidCompression=yes

[Files]
Source: "out\*.whl"; DestDir: "{app}\wheels"; Flags: ignoreversion

[Run]
Filename: "{app}\wheels\python.exe"; Parameters: "-m pip install --upgrade dahood-scripts"; Flags: runhidden