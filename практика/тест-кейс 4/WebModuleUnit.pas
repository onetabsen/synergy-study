## 💻 Ключевые файлы Delphi (пример)

**WebModuleUnit.pas**:
```delphi
unit WebModuleUnit;

interface

uses
  System.SysUtils, System.Classes, Web.HTTPApp;

type
  TWebModule1 = class(TWebModule)
    procedure WebModule1DefaultHandlerAction(Sender: TObject;
      Request: TWebRequest; Response: TWebResponse; var Handled: Boolean);
  end;

var
  WebModuleClass: TComponentClass = TWebModule1;

implementation

{$R *.dfm}

procedure TWebModule1.WebModule1DefaultHandlerAction(Sender: TObject;
  Request: TWebRequest; Response: TWebResponse; var Handled: Boolean);
begin
  Response.Content := 
    '<html><head><title>Tourism WebApp</title></head>' +
    '<body><h1>Welcome to Tourism Web Application</h1></body></html>';
end;

end.