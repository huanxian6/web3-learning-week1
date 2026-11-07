Add-Type -AssemblyName System.Drawing

$basePath = (Get-Location).Path
$icoPath = Join-Path $basePath 'blockchain_career_icon.ico'

# Create 256x256 bitmap
$bmp = New-Object System.Drawing.Bitmap(256, 256)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.Clear([System.Drawing.Color]::FromArgb(255, 5, 5, 16))

# Pre-calculated hexagon points (center 128,128, radius 90)
$hexPts = @(
    (New-Object System.Drawing.PointF(128, 38)),   # top
    (New-Object System.Drawing.PointF(206, 83)),   # upper-right
    (New-Object System.Drawing.PointF(206, 173)),  # lower-right
    (New-Object System.Drawing.PointF(128, 218)),  # bottom
    (New-Object System.Drawing.PointF(50, 173)),   # lower-left
    (New-Object System.Drawing.PointF(50, 83))     # upper-left
)
$hexArray = [System.Drawing.PointF[]]($hexPts)

# Glow effect: draw multiple polygons with decreasing width
for ($w = 8; $w -ge 2; $w -= 2) {
    $alpha = [int](255 * (1 - ($w / 10)))
    $glowPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(60, 0, 240, 255), $w)
    $glowPen.LineJoin = [System.Drawing.Drawing2D.LineJoin]::Round
    $g.DrawPolygon($glowPen, $hexArray)
}

# Main hexagon outline (cyan)
$cyanPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(255, 0, 240, 255), 3)
$g.DrawPolygon($cyanPen, $hexArray)

# Inner hexagon (magenta, radius 55)
$innerPts = @(
    (New-Object System.Drawing.PointF(128, 73)),
    (New-Object System.Drawing.PointF(176, 101)),
    (New-Object System.Drawing.PointF(176, 155)),
    (New-Object System.Drawing.PointF(128, 183)),
    (New-Object System.Drawing.PointF(80, 155)),
    (New-Object System.Drawing.PointF(80, 101))
)
$innerArray = [System.Drawing.PointF[]]($innerPts)
$magentaPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(255, 255, 0, 222), 2)
$g.DrawPolygon($magentaPen, $innerArray)

# Center cube (gold)
$goldPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(255, 255, 215, 0), 3)
$g.DrawRectangle($goldPen, 100, 100, 56, 56)

# Inner cube
$innerCubePen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(180, 255, 215, 0), 2)
$g.DrawRectangle($innerCubePen, 110, 110, 36, 36)

# Connecting lines (cyan, from center to hexagon vertices)
$linePen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(100, 0, 240, 255), 1)
$g.DrawLine($linePen, 128, 128, 128, 100)
$g.DrawLine($linePen, 128, 128, 128, 156)
$g.DrawLine($linePen, 128, 128, 100, 128)
$g.DrawLine($linePen, 128, 128, 156, 128)

# Small corner accent dots
$dotBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(255, 0, 240, 255))
$g.FillEllipse($dotBrush, 22, 22, 8, 8)
$g.FillEllipse($dotBrush, 226, 22, 8, 8)
$g.FillEllipse($dotBrush, 22, 226, 8, 8)
$g.FillEllipse($dotBrush, 226, 226, 8, 8)

# Save as ICO
$hicon = $bmp.GetHicon()
$icon = [System.Drawing.Icon]::FromHandle($hicon)
$fs = [System.IO.File]::Create($icoPath)
$icon.Save($fs)
$fs.Close()
$g.Dispose()
$bmp.Dispose()

# Update the shortcut icon
$desktopPath = [Environment]::GetFolderPath('Desktop')
$lnkPath = Join-Path $desktopPath 'BLOCKCHAIN CAREER OS.lnk'
$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($lnkPath)
$shortcut.TargetPath = Join-Path $basePath 'blockchain_career_dashboard.html'
$shortcut.IconLocation = $icoPath
$shortcut.Description = 'Blockchain Career OS'
$shortcut.Save()

$icoSize = (Get-Item $icoPath).Length
Write-Output "Icon created: $icoPath ($icoSize bytes)"
Write-Output "Shortcut updated: $lnkPath"
