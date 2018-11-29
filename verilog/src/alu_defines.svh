typedef enum logic [`alu_ctrl_size:0] {  
        
        // Arithmetic controls
        alu_op_add,
		alu_op_sub,
        alu_op_sll,
        alu_op_srl,
        alu_op_sra,

        // Boolean controls
		alu_op_and,
		alu_op_or,
		alu_op_xor,
        alu_op_not,

        // Invalid, always kept last
        alu_op_invalid
} alu_ops_t;