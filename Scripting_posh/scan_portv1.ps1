#Brian Reyna Castillo 2127309


$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host ' == Determinando tu gateway ... '
Write-Host 'Tu gateway es : ' $subred
$rango = $subred.Substring(0,$subred.Indexof('.')+ 1 + $subred.Substring($subred.Indexof('.')+1).Indexof('.')+3)
Write-Host "Determinnado tu rango de subred ..."
Write-Host $rango
$punto = $rango.EndsWith('.')
if ($punto -like 'False') {
    $rango = $rango + '.'
}
 $portstoscan = @(20,21,22,23,24,25,50,51,53,80,110,119,135,136,137,138,139,143,161,162,389,443,445,636,1025,1443,3389,5985,5986,8080,10000)
 $waittime = 100
 
 Write-Host 'Direccion ip a escanear ' -NoNewline
 $direccion = Read-Host

 foreach($p in $portstoscan )
 { 
    $TCPObject = New-Object System.Net.Sockets.TcpClient
        try{ $resultado =  $TCPObject.ConnectAsync($direccion,$p).Wait($waittime)}catch{}
        if ($resultado -eq "True") {
            Write-Host "Puerto abierto :" -NoNewline; Write-Host $p -ForegroundColor Green
            
        }


 }