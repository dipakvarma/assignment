import textwrap
sample_text ='''        
        hello
        world
        welcome        
        '''
text_without_Indentation = textwrap.dedent(sample_text)
#wrapped = textwrap.fill(text_without_Indentation)
final_result = textwrap.indent(text_without_Indentation, '> ')
print(final_result)

