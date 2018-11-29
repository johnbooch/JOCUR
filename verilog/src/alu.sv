`include "ALU.svh"

module ALU
#(
    DATA_WIDTH = 16
)
(
    input logic [DATA_WIDTH:0] ain,
    input logic [DATA_WIDTH:0] bin,
    input alu_opt_t control,
    output logic [DATA_WIDTH:0] result
);

    always_comb begin
        
        case (control)

            alu_control_add: begin

            end

            alu_control_sub: begin

            end

            alu_control_and: begin

            end
            alu_op_sll: begin

            end
            
            alu_op_srl: begin
                
            end
            
            alu_op_sra: begin
                
            end

            alu_control_or: begin

            end

            alu_control_xor: begin

            end

            alu_control_not: begin

            end
            
            default: begin
                pass
            end
        endcase
    end

endmodule // ALU