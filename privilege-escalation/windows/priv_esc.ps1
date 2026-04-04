try {
    throw "error"
} catch {
    while ( -not $? ){
        try{
            Start-Process cmd.exe -Verb RunAs
        } catch {
            Get-ChildItem "gfgsnvsdnfnln"
        }
    }
}
