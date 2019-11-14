Attribute VB_Name = "Module1"
Sub dataloop():
Dim ws As Worksheet
Dim count As Long
Dim ticker As String
Dim yearly_change As Double
Dim percent_change As Double
Dim total_volumn As Double
Dim open_price As Double
Dim close_price As Double




LastRow = Cells(Rows.count, 1).End(xlUp).row

For Each ws In Worksheets
    ws.Cells(1, 9).Value = "Ticker"
    ws.Cells(1, 10).Value = "Yearly Change"
    ws.Cells(1, 11).Value = "Percent Change"
    ws.Cells(1, 12).Value = "Total stock Volume"
    count = 2
    starting_row = 2
    
    For i = 2 To LastRow
        If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1) Then
            ws.Cells(count, 9).Value = ws.Cells(i, 9).Value
            open_price = ws.Cells(starting_row, 3).Value
            close_price = ws.Cells(i, 6).Value
            
            For j = i To LastRow
    
            If open_price = 0 Then
        
            open_price = ws.Cells(starting_row + 1, 3).Value
        
            
            End If
        
            Next j
            
            ws.Cells(count, 10).Value = close_price - open_price
            
            If ws.Cells(count, 10).Value > 0 Then
            
                ws.Cells(count, 10).Interior.ColorIndex = 4
                
            ElseIf ws.Cells(count, 10) < 0 Then
            
                ws.Cells(count, 10).Interior.ColorIndex = 3
                
                End If
                
            If close_price <> 0 And open_price <> 0 Then
                ws.Cells(count, 11).Value = ws.Cells(count, 10).Value / open_price
    
                ws.Cells(count, 12).Value = WorksheetFunction.sum(Range("G" & count & ":" & "G" & i))
        
            End If
            
            starting_row = starting_row + 1
            count = i + 1
            
            End If
        Next i
    Next ws
End Sub
