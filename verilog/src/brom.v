module BROM 
    #( 
        DATA_WIDTH = 32,
        BROM_DEPTH = 256
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

    reg [DATA_WIDTH-1:0] ROM[0:BROM_DEPTH-1];

    assign dout = ROM[addr];

    assign busy =  ce ? 1'b1 ? 1'bZ


    always(@posedge ck) begin
        if(wen && ce) begin
            ROM[addr] <= din;
        end
    end

endmodule // BROM