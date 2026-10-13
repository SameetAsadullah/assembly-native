<h1 align="center">Checker Board in Assembly</h1>

### Description
An interactive 5×5 checkerboard rendered in x86 assembly with keyboard- and mouse-driven color updates. Uppercase keyboard input highlights matching lettered squares in green; mouse selection changes black squares to red and white squares to blue.

### Manual
1) Use these command in dosbox to `Compile` and `Run` the code:
    ```
    ml main.asm
    ```
    ```
    main.exe
    ```
    
    <div align="center">
      <img src="extras/commands-ss.png" alt="DOSBox commands used to build the checker board" width="600px"/>
    </div>

2) For `Keyboard Input`, press `CapsLock` and then `Type Your Name`. You will see those squares turning into green:
    <div align="center">
      <img src="extras/working-ss-1.png" alt="Keyboard interaction with the checker board" width="600px"/>
    </div>
    
3) To change the code and make it `Work for Your Name`, you must replace the alphabets of my name with yours here:
    <div align="center">
      <img src="extras/code-ss.png" alt="Checker board name configuration in the source" width="600px"/>
    </div>
    
4) For `Mouse Input`, click on any square you want. Black squares will turn red and white squares will turn blue:
    <div align="center">
      <img src="extras/working-ss-2.png" alt="Mouse interaction with the checker board" width="600px"/>
    </div>
