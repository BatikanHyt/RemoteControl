$username = "abcd"
$password = "secret"
$secstr = New-Object -TypeName System.Security.SecureString
$password.ToCharArray() | ForEach-Object {$secstr.AppendChar($_)}
$cred = new-object -typename System.Management.Automation.PSCredential -argumentlist $username, $secstr

function getService{
    Invoke-Command -ComputerName MachineName -ScriptBlock { Get-Service } -Credential $cred
}
getService
