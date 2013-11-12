Useful XBee S1 commands
---

<table>
    <tbody>
      <tr>
        <td>
          <strong>Command</strong>
        </td>
        <td>
          <strong>Description</strong>
        </td>
        <td>
          <strong>Valid Values</strong>
        </td>
        <td>
          <strong>Default Value</strong>
        </td>
      </tr>
      <tr>
        <td>ID</td>
        <td>The network ID of the Xbee module.</td>
        <td>0 - 0xFFFF</td>
        <td>3332</td>
      </tr>
      <tr>
        <td>CH</td>
        <td>The channel of the Xbee module.</td>
        <td>0x0B - 0x1A</td>
        <td>0X0C</td>
      </tr>
      <tr>
        <td>SH and SL</td>
        <td>
          The serial number of the Xbee module (SH gives the high 32 bits, SL the low 32 bits).
          <br>
          Read-only.
        </td>
        <td>
          0 – 0xFFFFFFFF
          <br>
          (for both SH and SL)
        </td>
        <td>different for each module</td>
      </tr>
      <tr>
        <td>MY</td>
        <td>The 16-bit address of the module.</td>
        <td>0 - 0xFFFF</td>
        <td>0</td>
      </tr>
      <tr>
        <td>DH and DL</td>
        <td>
          The destination address for wireless communication (DH is the high 32 bits, DL the low 32).
        </td>
        <td>
          0 – 0xFFFFFFFF
          <br>
          (for both DH and DL)
        </td>
        <td>0 (for both DH and DL)</td>
      </tr>
      <tr>
        <td>BD</td>
        <td>
          The baud rate used for serial communication with the Arduino board or computer.
        </td>
        <td>
          0 (1200 bps)
          <br>
          1 (2400 bps)
          <br>
          2 (4800 bps)
          <br>
          3 (9600 bps)
          <br>
          4 (19200 bps)
          <br>
          5 (38400 bps)
          <br>
          6 (57600 bps)
          <br>
          7 (115200 bps)
        </td>
        <td>3 (9600 baud)</td>
      </tr>
    </tbody>
  </table>

> Note: although the valid and default values in the table above are written with a prefix of `0x` (to indicate that they are hexadecimal numbers), the module will not include the `0x` when reporting the value of a parameter, and you should omit it when setting values. 

  <table>
    <tbody>
      <tr>
        <td>
          <strong>Command</strong>
        </td>
        <td>
          <strong>Description</strong>
        </td>
      </tr>
      <tr>
        <td>RE</td>
        <td>
          Restore factory default settings (note that like parameter changes, this is not permanent unless followed by the WR command).
        </td>
      </tr>
      <tr>
        <td>WR</td>
        <td>
          Write newly configured parameter values to non-volatile (long-term) storage. Otherwise, they will only last until the module loses power.
        </td>
      </tr>
      <tr>
        <td>CN</td>
        <td>
          Exit command mode now. (If you don't send any commands to the module for a few seconds, command mode will timeout and exit even without a CN command.)
        </td>
      </tr>
    </tbody>
  </table>