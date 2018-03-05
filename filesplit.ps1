$Path = "C:\Thesis\Addresses"
$InputFile = (Join-Path $Path "stateoftheunion1790-2016.txt")
$Reader = New-Object System.IO.StreamReader ($InputFile)

While (($Line = $Reader.ReadLine()) -ne $null) {
    If ($Line -match "\*\*\*") {
        $Year = 1789
        $OutputFile = $year + ".txt"
        $Year++
    }

    Add-Content (Join-Path $Path $OutputFile) $Line
}