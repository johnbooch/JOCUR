module BRAM 
    #(
        DATA_WIDTH = 32,
        BRAM_DEPTH = 256;
    );
    (
        input ck;
        input [DATA_WIDTH-1:0] addr;
        input [DATA_WIDTH-1:0] din;
        input wen;
        input ce;
        output [DATA_WIDTH-1:0] dout;
        output busy;
    );

    reg [DATA_WIDTH-1:0] RAM[0:BRAM_DEPTH-1];

    assign dout = RAM[addr];

    assign busy =  ce ? 1'b1 ? 1'bZ
    
    always(@posedge ck) begin
        if(wen && ce) begin
            RAM[addr] <= din;
        end
    end

endmodule // RAM