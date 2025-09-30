import gradio as gr

def predict(text):
    return f"Hello : {text}"

demo = gr.Interface(fn=predict, inputs="text", outputs="text")

if __name__ == "__main__":
    demo.launch()