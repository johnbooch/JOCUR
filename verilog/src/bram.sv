module BRAM (
    input ck;
    input [DATA_WIDTH:0] addr;
    input [DATA_WIDTH:0] din;
    input wen;
    output [DATA_WIDTH:0] dout;
);

    reg [DATA_WIDTH:0] RAM[0:BRAM_WIDTH];

    assign dout = RAM[addr];

    always(@posedge ck) begin
        if(wen) begin
            RAM[addr] <= din;
        end
    end

endmodule // RAM