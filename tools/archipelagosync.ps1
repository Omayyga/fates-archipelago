param(
    [string]$ArchipelagoPath = "F:\Projects\Archipelago"
)

$SourceWorld = "F:\Projects\fates-archipelago\worlds\fates"
$TargetWorld = Join-Path $ArchipelagoPath "worlds\fates"

Write-Host "Syncing Fates world to Archipelago test folder..."
Write-Host "Source: $SourceWorld"
Write-Host "Target: $TargetWorld"

if (!(Test-Path $ArchipelagoPath)) {
    Write-Error "Archipelago path does not exist: $ArchipelagoPath"
    exit 1
}

if (!(Test-Path $SourceWorld)) {
    Write-Error "Source world path does not exist: $SourceWorld"
    exit 1
}

if (Test-Path $TargetWorld) {
    Remove-Item -Recurse -Force $TargetWorld
}

Copy-Item -Recurse -Force $SourceWorld $TargetWorld

Write-Host "Done."