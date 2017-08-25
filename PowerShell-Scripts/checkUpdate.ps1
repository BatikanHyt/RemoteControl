$username = "abcd"
$password = "secret"
$secstr = New-Object -TypeName System.Security.SecureString
$password.ToCharArray() | ForEach-Object {$secstr.AppendChar($_)}
$cred = new-object -typename System.Management.Automation.PSCredential -argumentlist $username, $secstr
function checkUpd{
#Define update criteria.
$Criteria = "IsInstalled=0 and Type='Software'"

#Search for relevant updates.
$Searcher = New-Object -ComObject Microsoft.Update.Searcher
$SearchResult = $Searcher.Search($Criteria).Updates

If($SearchResult.Count -eq 0){
Write-Host "No Updates Available"
Exit
}

Write-Host "Updates Found: $($SearchResult.Count)`r`n"
$SearchResult | ForEach-Object{Write-Host "$($_.Title) `r`n"}
}

Invoke-Command -ComputerName MachineName -ScriptBlock $function:checkUpd -Credential $cred