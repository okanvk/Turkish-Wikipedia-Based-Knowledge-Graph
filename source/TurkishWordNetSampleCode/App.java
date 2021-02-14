package App;

import WordNet.WordNet;
import WordNet.SynSet;

import java.io.IOException;
import java.util.*;
import java.io.FileWriter;


public class App {
    public static void main(String[] args) throws IOException {

        WordNet a = new WordNet();


        Collection<SynSet> list = a.synSetList();


        Set<String> adjectives = new HashSet<>();
        Set<String> adverbs = new HashSet<>();
        Set<String> verbs = new HashSet<>();


        for (SynSet item : list) {

            if (item.getPos().name().equals("ADJECTIVE")) {
                adjectives.add(item.representative());
            }
            if (item.getPos().name().equals("ADVERB")) {
                adverbs.add(item.representative());
            }
            if (item.getPos().name().equals("VERB")) {
                verbs.add(item.representative());
            }

        }

        writeDataToTxt("tr_adjectives.txt", adjectives);
        writeDataToTxt("tr_adverbs.txt", adverbs);
        writeDataToTxt("tr_verbs.txt", verbs);

        System.out.println(verbs.size());

        System.out.println(adverbs.size());
        System.out.println(adjectives.size());

    }



    public static void writeDataToTxt(String fileName,Set<String> data) throws IOException {

        FileWriter writer = new FileWriter(fileName);
        for(String str: data) {
            writer.write(str + System.lineSeparator());
        }
        writer.close();
    }

}
