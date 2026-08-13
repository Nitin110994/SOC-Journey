# Day 23 – PowerShell Investigation

## Objective

Investigate suspicious PowerShell process creation activity using Sysmon logs in Splunk.

## What I Investigated

- PowerShell process creation
- Encoded PowerShell commands
- Process IDs and parent process IDs
- PowerShell process tree
- Base64 encoded command
- Related PowerShell activity

## Tools Used

- Splunk Enterprise
- Windows
- Sysmon
- PowerShell

## Key Finding

A PowerShell process with PID `4508` was found using the `-EncodedCommand` parameter.

I traced the process back to its parent PowerShell process and then back to `explorer.exe`.

The encoded command was decoded and found to be:

```text
Get-Process

This is a normal PowerShell command used to retrieve running processes.

Final Classification

Benign / False Positive

Investigation Report

The detailed investigation and analysis are documented in:

PowerShell Investigation Report
